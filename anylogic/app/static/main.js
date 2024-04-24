  window.csrfTokenName = "{{ craft.config.csrfTokenName }}";
  window.csrfTokenValue = "{{ craft.request.csrfTokenValue }}";

  var x = document.getElementById("myDIV");
  var y = document.getElementById("mainele");
  var z = document.getElementById("mobile-menu-3");
  var k = document.getElementById("divSearch");
  var l = document.getElementById("dropdown");
  var close_l = document.getElementById("user-menu-button");
  var close_x = document.getElementById("sideBtn");
  var focusSearch = document.getElementById("searchInput");
  var maindiv = document.getElementById("maindiv");
  var mainele = document.getElementById("mainele");
  var overlay = document.getElementById("my-modal");
  
  function myFunction() {
    if (x.style.display === "block") {
      x.style="display: block; animation: remove 0.5s ease-in-out; animation-iteration-count: 1;"
      let timer
      clearTimeout(timer);
        timer = setTimeout(() =>{
          x.dataavailable = "false";
          x.style.display = "none";
          overlay.style.display = "none";
          maindiv.style = 'pointer-events: auto;';
    }, 400);
      console.log("prva 1")
    } else {
      x.style="display: block; animation: move 0.5s ease-in-out; animation-iteration-count: 1;"
      x.dataavailable = "true";
      overlay.style.display = "block";
      console.log("prva 2")
      maindiv.style = 'pointer-events: none;';
    }
  }

  function myFunctionSeach() {
    if (z.style.display === "block") {
      z.style.display = "none";
      z.dataavailable = "false";
    } else {
      z.style.display = "block";
      z.dataavailable = "true";
    }
  }

  function myFunctionDropdown() {
    if (l.style.display === "block") {
      l.style.display = "none";
      l.dataavailable = "false";
      //y.style.pointerEvents = 'auto';
    } else {
      l.style = 'display: block;';
      l.dataavailable = "true";
      //y.style.pointerEvents = 'none';
    }
  }

  window.onclick = function(event) {
    var newWidth = window.innerWidth;
      if (event.target != close_l && event.target != l && l.style.display === "block") {
        l.style.display = "none";
        console.log("mnaruga")
      }

      if (newWidth < 1024 && event.target != close_x && event.target != x && x.style.display === "block") {
        x.style="display: block; animation: remove 0.5s ease-in-out; animation-iteration-count: 1;"
        console.log("onclick")
      let timer
      clearTimeout(timer);
        timer = setTimeout(() =>{
          x.dataavailable = "false";
          x.style.display = "none";
          overlay.style.display = "none";
          maindiv.style = 'pointer-events: auto;';
        }, 400);
        console.log("druga")
      }
    }

