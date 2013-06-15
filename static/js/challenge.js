$(document).ready(function(){
    $.getJSON("/create",
        function(data){
          alert("test");
          if (data.res == 'out') {
            $("#set_challenge").click(function(){
            alert('set_challenge');
            });
            $("reset").click(function(){
            alert('reset');
            });
          } 
        });
  });