window.addEventListener('load', (event) => {
  console.log('page is fully loaded');
});




function displayColumn(){
  let displayColumn = document.getElementById('displayColumn')
  let columnSelect = document.getElementById('columnSelect').value
  displayColumn.innerText =  columnSelect;
}

function displayOperation(){
  let displayOperation = document.getElementById('displayOperation')
  let operationSelect = document.getElementById('operationSelect').value
  displayOperation.innerText =  operationSelect;

}

function displayHowMany(){
  let displayHowMany = document.getElementById('displayHowMany')
  let howManySelect = document.getElementById('howManySelect').value
  displayHowMany.innerText =  howManySelect;

}


function displayPrice(){
  let displayPrice = document.getElementById('displayPrice')
  let priceSelect = document.getElementById('priceSelect').value
  displayPrice.innerText =  priceSelect;

}

function displayText(){
  let displayText = document.getElementById('displayText')
  let textSelect = document.getElementById('textSelect').value
  displayText.innerText =  "\"" + textSelect + "\"";

}