var x=21.144453;
var y=79.054140;
var cen=new google.maps.LatLng(x,y);
var map1="";
var cen1="";
function doo(){
map1.panTo(cen1);
}
function initialize(){
var mapOptions={
zoom:17,
center:cen,
mapTypeId:google.maps.MapTypeId.ROADMAP

}
map=new google.maps.Map(document.getElementById('map-canvas'),mapOptions);

var image = "static/images/bus.png";
marker=new google.maps.Marker({
position:cen,
map:map,
icon:image
});
moveMarker(map,marker);
map1=map;

}
function moveMarker(map,marker){
setInterval(function(){
//x+=0.0001;
//y+=0.0001;
center = new google.maps.LatLng(x,y);
cen1=center;
//alert(x);
marker.setPosition(cen1);
},100);
}
google.maps.event.addDomListener(window,'load',initialize);
$(document).ready(function(){

function only(){
    $.ajax({
            url: '/getValues',
            type: 'GET',
            datatype:'json',
          
            success: function(response) {
                var a = response.split(',');
                var d=a[0].split(":")
                var e=a[1].split(":")
                a = d[1].split('"');
                d=a[1].split(',');
                var c=e[1].split('}');
                e=c[0].split('"');
                c=e[1].split(',');
                
                //alert(a);
                x=d;
                y=c;
                },
            error: function(error) {
                //alert(error);
            }
        });
//moveMarker();
 }
setInterval(only,1000);

});
