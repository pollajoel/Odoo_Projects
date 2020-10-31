window.addEventListener('load', function () {
	
var currentTab = 0; // Current tab is set to be the first tab (0)
showTab(currentTab); // Display the current tab

//onclick="nextPrev(-1)"
$( "#prevBtn" ).click(function() {
	nextPrev(-1)
  //alert( "Handler for .click() called." );
});

$( "#nextBtn" ).click(function() {
	nextPrev(1);
  //alert( "Handler for .click() called." );
});



function showTab(n) {
  // This function will display the specified tab of the form...
  
  if( document.getElementsByClassName("tab") != undefined )
  {
	  
  var x = document.getElementsByClassName("tab");
  
  if( x[n] != undefined )
	{
  
  x[n].style.display = "block";
  //... and fix the Previous/Next buttons:
  if (n == 0) {
    document.getElementById("prevBtn").style.display = "none";
  } else {
    document.getElementById("prevBtn").style.display = "inline";
  }
  if (n == (x.length - 1)) {
    document.getElementById("nextBtn").innerHTML = "VALIDER";
  } else {
    document.getElementById("nextBtn").innerHTML = "SUIVANT";
  }
  //... and run a function that will display the correct step indicator:
  fixStepIndicator(n)
  
	}
  
  }
}

function nextPrev(n) {
	
	
  if( document.getElementsByClassName("tab") != undefined )
  {
	
  // This function will figure out which tab to display
  var x = document.getElementsByClassName("tab");
  // Exit the function if any field in the current tab is invalid:
  if (n == 1 && !validateForm()) return false;
  // Hide the current tab:
  x[currentTab].style.display = "none";
  // Increase or decrease the current tab by 1:
  currentTab = currentTab + n;
  // if you have reached the end of the form...
  if (currentTab >= x.length) {
    // ... the form gets submitted:
    document.getElementById("regForm").submit();
    return false;
  }
  // Otherwise, display the correct tab:
  showTab(currentTab);
  
  }
}

function validateForm() {
  
  
  if( document.getElementsByClassName("tab") != undefined )
  {
  
  // This function deals with validation of the form fields
  var x, y, i, valid = true;
  x = document.getElementsByClassName("tab");
  y = x[currentTab].getElementsByTagName("input");
  // A loop that checks every input field in the current tab:
  console.log(y);
  for (i = 0; i < y.length; i++) {
    // If a field is empty...
    if ( ((y[i].value == "") && (y[i].name!="profphone")) &&((y[i].value == "") &&(y[i].name!="nomassociation")) ){
      // add an "invalid" class to the field:
      y[i].className += " invalid";
      // and set the current valid status to false
      valid = false;
    }
	
	if( y[i].name == "cud" || y[i].name == "cud0" || y[i].name == "cud1" ){
		
		 y[i].className += " invalid";
		 
		 alert( y[i].value );
		 
		 valid = false;
		 //document.getElementById("Cudobigatoire").style.display = "block";
		
		
	}
		
	
	
	
  }
  // If the valid status is true, mark the step as finished and valid:
  if (valid) {
    document.getElementsByClassName("step")[currentTab].className += " finish";
  }
  return valid; // return the valid status

}  

}



function fixStepIndicator(n) {
  // This function removes the "active" class of all steps...
  var i, x = document.getElementsByClassName("step");
  for (i = 0; i < x.length; i++) {
    x[i].className = x[i].className.replace(" active", "");
  }
  //... and adds the "active" class on the current step:
  x[n].className += " active";
}
















function doAnimations(elems) {
  var animEndEv = 'webkitAnimationEnd animationend';

  elems.each(function () {
    var $this = $(this),
        $animationType = $this.data('animation');

    // Add animate.css classes to
    // the elements to be animated
    // Remove animate.css classes
    // once the animation event has ended
    $this.addClass($animationType).one(animEndEv, function () {
      $this.removeClass($animationType);
    });
  });
}









  
  
  
 

  
 
 







	
	
	
	
	
	
	
});