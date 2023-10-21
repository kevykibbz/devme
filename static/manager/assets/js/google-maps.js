function initMap() {
    // Latitude and Longitude
    var myLatLng = {lat:-1.2349006, lng: 36.8850074};

    var map = new google.maps.Map(document.getElementById('google-maps'), {
        zoom: 17,
        center: myLatLng
    });

    var marker = new google.maps.Marker({
        position: myLatLng,
        map: map,
        title: 'Nairobi, Kenya' // Title Location
    });
}