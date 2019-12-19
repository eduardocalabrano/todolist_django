$(document).ready(function(){
  // $(".campos_new_user").val('');

  $(".botBorrarUsuario" ).click(function() {
    // alert(this.dataset.usuario_del);
    $.ajax({
        url: 'ajax/borra/usuario/',
        data: {
          'id': this.dataset.usuario_del
        },
        dataType: 'json',
        success: function (data) {
          // alert(data.respuesta);
          // window.location.reload();
        }
      });
  });
});
