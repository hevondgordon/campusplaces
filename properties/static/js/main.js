
function initMap() {
  var jamaica = {lat: 17.9926785, lng: -76.9684947};
  var map = new google.maps.Map(document.getElementById('map'), {
    zoom: 13,
    center: jamaica
  });
  var marker = new google.maps.Marker({
    position: jamaica,
    map: map
  });
}

// $("#rangeslider").ionRangeSlider({
//     type: "double",
//     min: 0,
//     max: 100000,
//     from: 30,
//     to: 7000,
//     grid: true
// });

$('.icon').click(function(){
  var mobile_nav =$('#mobile-nav')
  if(mobile_nav.hasClass('responsive')){
    mobile_nav.removeClass('responsive')
  }
  else{
    mobile_nav.addClass("responsive");
  }
  return false;
});

$('.mini-card').click(function(){
  currently_active = $('.active-mini-card')
  currently_active.removeClass('active-mini-card')
  $(this).addClass('active-mini-card');
  $('#accomodation').val($(this).attr('id'));
  $('label.active-tick').removeClass('active-tick');
  $(this).find('label.tick').addClass('active-tick');

});

// console.info('{{ to }}')