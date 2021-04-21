var AtbashWheel = {};

// Creating Atbash mapping of a -> z, b -> y and so on
for(i = 65, j = 0; i <= 90; i++, j++)
{
  AtbashWheel[String.fromCharCode(i)] = String.fromCharCode(90 - j);
}
// Creating Atbash mapping of A -> Z, B -> Y and so on
for(i = 97, j = 0; i <= 122;i++,j++)
{
  AtbashWheel[String.fromCharCode(i)] = String.fromCharCode(122 - j);
}

//Calls the Cipher function when text written on the box
function checkInput(obj) {
  AtbashCipher(obj.value)
}

//Since symmetric, encryption and decryption works through the same function
function AtbashCipher(txt){
  
  inputText = document.getElementById("input1").value;
  outputText = "";
  
  //Checking if inputText is empty
  if(inputText.length==0)
    document.getElementById("input2").value = "";
  
  for( i=0;i<inputText.length;i++)
  {
    // Checking if the character is in [a-z] or [A-Z] 
    if( AtbashWheel[inputText[i]] !== undefined ) {
      res += AtbashWheel[inputText[i]];  
    }
    //Checking if character non alphabetic
    else {
      //No change, use the same character
      res += inputText[i];
    }
    document.getElementById("input2").value = res;
  }
}

var is_swapped = 0

function swapPlainAndCipher(){
  if(is_swapped == 0)
  {
    document.getElementById("input1").placeholder = "Cipher Text";
    document.getElementById("input2").placeholder = "Plain Text";
    document.getElementById("input1").value = "";
    document.getElementById("input2").value = "";
    document.getElementById("swap").innerHTML = "Change to Encryption";
  }
  else{
    document.getElementById("input1").placeholder = "Plain Text";
    document.getElementById("input2").placeholder = "Cipher Text";
    document.getElementById("input1").value = "";
    document.getElementById("input2").value = "";
    document.getElementById("swap").innerHTML = "Change to Decryption";
  }
  is_swapped ^= 1
}
