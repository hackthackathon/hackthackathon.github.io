function renderMap() {
  const map = L.map('map').setView([20, 0], 2);
  map.createPane('topDots');
  map.getPane('topDots').style.zIndex = 650;

  map.whenReady(() => {
    const bounds = map.getBounds();
    map.setMaxBounds(bounds);            // prevent panning outside the initial area
    map.setMinZoom(map.getZoom());       // prevent zooming out
    map.options.maxBoundsViscosity = 1.0; // smooth bounce-back effect
  });

  L.tileLayer('https://tiles.wmflabs.org/bw-mapnik/{z}/{x}/{y}.png', {
    attribution: '',
    maxZoom: 18
  }).addTo(map);

  fetch("https://raw.githubusercontent.com/datasets/geo-boundaries-world-110m/master/countries.geojson")
  .then(response => response.json())
  .then(geojson => {
    L.geoJSON(geojson, {
      style: {
        color: "#d3d3d3",
        weight: 1.5,
        opacity: 1,
        fillColor: "#000000",
        fillOpacity: 0.7
      }
    }).addTo(map);
  });

  const markers = L.markerClusterGroup({
    showCoverageOnHover: false
  });

  locations.forEach(loc => {
    const circle = L.circleMarker([loc.lat, loc.lng], {
      radius: 6,
      color: '#ff0000',
      fillColor: 'transparent',
      fillOpacity: 0,
      weight: 3,
      pane: 'topDots'
    }).bindPopup(`<b>${loc.name}</b>`);

    markers.addLayer(circle);
  });

  map.addLayer(markers);
}
