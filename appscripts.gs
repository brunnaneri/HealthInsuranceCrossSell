function onOpen(){
  var ui = SpreadsheetApp.getUi();
  ui.createMenu('Propensity Score')
    .addItem('Get Prediction','PredictAll')
    .addToUi();
}


// Helper Function

host_production = 'healt-insurance-app.herokuapp.com'

function ApiCall(data,endpoint){
  var url = 'https://'+ host_production + endpoint;
  var payload = JSON.stringify(data);

  var options = {'method': 'POST', 'contentType': 'application/json', 'payload': payload};
  Logger.log( url )
  Logger.log( options )

  var response = UrlFetchApp.fetch(url, options);

  var rc = response.getResponseCode();
  var responseText = response.getContentText();
  if (rc !== 200){
    Logger.log('Response (%s)%s',rc,responseText)
  }
  else{
    prediction = JSON.parse(responseText);
  }
  return prediction
};

// Function Sort

function SortPred(){
 var ss = SpreadsheetApp.getActiveSpreadsheet();
 var sheet = ss.getSheets()[0];
 var lastRow = sheet.getLastRow();
 var lastColumn = sheet.getLastColumn();
 var range = sheet.getRange('A2' + ':' + 'L' + lastRow);
 range.sort({column: lastColumn, ascending: false});
}

// Function Predict All

function PredictAll(){
  var ss = SpreadsheetApp.getActiveSheet();
  var titleColumns = ss.getDataRange().getValues()[0];
  var data = ss.getDataRange().getValues();
  data.shift();
 
  //Logger.log(data)
  
  for (row in data){
    var json = new Object();
    
    for(var j=0; j < titleColumns.length; j++){
      json[titleColumns[j]] = data[row][j];
    };
  
  //Json file to send
    var json_send = new Object();				
    json_send['id'] = json['id']
    json_send['gender'] = json['gender']
    json_send['age'] = json['age']
    json_send['driving_license'] = json['driving_license']
    json_send['region_code'] = json['region_code']
    json_send['previously_insured'] = json['previously_insured']
    json_send['vehicle_age'] = json['vehicle_age']
    json_send['vehicle_damage'] = json['vehicle_damage']
    json_send['annual_premium'] = json['annual_premium']
    json_send['policy_sales_channel'] = json['policy_sales_channel']
    json_send['vintage'] = json['vintage']
    
    
    pred = ApiCall(json_send,'/predict');

    Logger.log(pred)

    // Send back to google sheets
    ss.getRange( Number( row ) + 2 , titleColumns.length ).setValue( pred[0]['predict_score'] )


  };
    // call sort function
  SortPred()
  
};
