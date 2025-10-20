function renderMap() {
  const map = L.map('map').setView([20, 0], 2);

  L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 10,
    attribution: '© OpenStreetMap contributors'
  }).addTo(map);

  const markers = L.markerClusterGroup();

  locations.forEach(loc => {
    const marker = L.marker([loc.lat, loc.lng])
      .bindPopup(`<b>${loc.name}</b>`);
    markers.addLayer(marker);
  });

  map.addLayer(markers);
}
