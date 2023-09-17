var CSRFToken = '{{ csrf_token }}' 

  $(document).ready(function(){
  $('#logout-button').on('click',function(e){
    e.preventDefault();
      $.ajax({
        url :'/Accounts/logout/',
        type: 'POST',
        headers:{
          'X-CSRFToken': CSRFToken
        },
        success : function(response){
          if (response.success){
            $('#logged-in').hide()
          }
        }
      });
  });
});