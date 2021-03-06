$(function () {

  // sorce: http://stackoverflow.com/a/22172860
  function getBase64Image(img) {
    var canvas = document.createElement("canvas");
    canvas.width = img.width;
    canvas.height = img.height;
    var ctx = canvas.getContext("2d");
    ctx.drawImage(img, 0, 0);
    var dataURL = canvas.toDataURL("image/jpeg");
//    console.log(dataURL)
    return dataURL.replace(/^data:image\/(png|jpg|jpeg);base64,/, "");
  }

  $('.thumbnail img')
    .click(function () {
      var btm_img = $(this).attr('src');
      $('#img_plc').attr('src', btm_img);
    });

  $("#clk").on('click', function (event) {
    $('#txt_area').hide();
    $('#meow').show();
    var tmp_img = document.createElement("img");
    tmp_img.src = 'http://'+location.host+$('#img_plc').attr('src');
    var base64 = getBase64Image(tmp_img);
    $.ajax({
      type: "POST",
      url: "http://localhost:5000/api/predict",
      data: { imageBase64: base64 },
      success: function (result) {
        var res = result.results[0];
        var cal=result.results[1];



        $('#meow').hide();
        $('#txt_area').text("Image is predicted as  "+res+" and calories = "+cal);

        $('#txt_area').show();
      }
    });
  });
});
