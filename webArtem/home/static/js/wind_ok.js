$("#data-form").on('submit', function(event){
  let data_form = $('#data-form').serialize();
  send(data_form);
  event.preventDefault();
})
function send(data_form){
  $.ajax({
    url:'',
    method: "POST",
    data: data_form,
    success: function(data){
      swal({
        text: "Ваш заказ принят!",
        icon: "success",
            });
        $('#id_name').val('');
        $('#id_telephone').val('');
            },
});
}

// var order_ok = document.getElementById("order-ok");
//   order_ok.addEventListener('click', function(){
// $('#order-ok').on('submit',function(event){
//     console.log('ok!');
//     let data_form = $('#data-form').serialize();
//     $.ajax({
//       url:'',
//       method:"post",
//       data: data_form,
//       success: function(data){
//         console.log('ok222!');
//         swal({
//           text: "Ваш заказ принят!",
//           icon: "success",
//         });
//       }
//     });
//     event.preventDefault();
//   })
