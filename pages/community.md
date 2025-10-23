<!--
.. title: Community
.. slug: community
.. hide_title: false
.. date: 2024-11-21 19:32:05 UTC
.. tags: 
.. category: 
.. link: 
.. description: 
.. type: text
.. extra_head: <link rel="stylesheet" href="https://unpkg.com/leaflet/dist/leaflet.css" /><link rel="stylesheet" href="https://unpkg.com/leaflet.markercluster/dist/MarkerCluster.css" /><link rel="stylesheet" href="https://unpkg.com/leaflet.markercluster/dist/MarkerCluster.Default.css" /><script src="https://unpkg.com/leaflet/dist/leaflet.js"></script><script src="https://unpkg.com/leaflet.markercluster/dist/leaflet.markercluster.js"></script><script src="/js/locations.js"></script><script src="/js/renderMap.js"></script><style>#map {width: 100%; height: 60vh; max-height: 800px; min-height: 300px;}</style></script><script src="/map-js/locations.js"></script><script src="/map-js/renderMap.js"></script><script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/3.9.1/chart.min.js"></script><link href="../style/visualization.css" rel="stylesheet" type="text/css"><script src="https://cdnjs.cloudflare.com/ajax/libs/d3/7.8.5/d3.min.js"></script><script src="https://unpkg.com/d3-sankey@0.12.3/dist/d3-sankey.min.js"></script>
-->

# Welcome to our community!

> Dive in to see [where we come from](#global-network) and [what interests us](#what-we-do). Explore [how our community has grown](#community-growth) and evolved through the different “Hack the Hackathon” events, and get to know the dedicated [steering group](#steering-committee) that helps guide our journey forward.

---

## Explore our Global Network {#global-network}

Each dot represents a city where our community has roots. Click on the larger clusters to zoom in, or tap a single circle to explore who’s part of our global network.

<div id="map"></div><script>renderMap();</script>

---

## Who We Are and What We Do {#what-we-do}

We come from a wide range of disciplines and bring equally diverse interests to our community.

The visualizations below highlight this diversity: one shows the various domains our participants represent across different “Hack the Hackathon” events, while the other illustrates the balance between hackathon organizers and researchers who take part in them.

Together, they offer a snapshot of the backgrounds, skills, and perspectives that shape our collaborative work.

<section class="py-5 bg-light">
    <div class="row text-center">
        <div class="col-md-6">
            <div id="error" class="error" style="display: none;"></div>
            <div id="timeline_ra" class="timeline"></div>
            <div class="main-card">
                <div class="nav-header">
                    <button id="prevBtn_ra" class="nav-btn">‹</button>
                    <h2 id="eventTitle_ra" class="event-title"></h2>
                    <button id="nextBtn_ra" class="nav-btn">›</button>
                </div>
                <div class="content-grid">
                    <div class="chart-container">
                        <canvas id="pieChart_DOMAIN"></canvas>
                    </div>
                    <div class="stats domains row">
                        <div class="col-md-5 stat-card total">
                            <div class="stat-label">Total Participants</div>
                            <div id="totalValueDomain" class="stat-value"></div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <div class="col-md-6">
            <div id="error" class="error" style="display: none;"></div>
            <div id="timeline_or" class="timeline"></div>
            <div class="main-card">
                <div class="nav-header">
                    <button id="prevBtn_or" class="nav-btn">‹</button>
                    <h2 id="eventTitle_or" class="event-title"></h2>
                    <button id="nextBtn_or" class="nav-btn">›</button>
                </div>
                <div class="content-grid">
                    <div class="chart-container">
                        <canvas id="pieChart_RO"></canvas>
                    </div>
                    <div class="stats ro">
                        <div class="stat-card practitioners">
                            <div class="stat-label">Practitioners</div>
                            <div id="practitionerPercent" class="stat-percent"></div>
                        </div>
                        <div class="stat-card researchers">
                            <div class="stat-label">Researchers</div>
                            <div id="researcherPercent" class="stat-percent"></div>
                        </div>
                        <div class="stat-card total">
                            <div class="stat-label">Total Participants</div>
                            <div id="totalValue" class="stat-value"></div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</section>


## How our Community Grows {#community-growth}

We are growing. The visualization below shows how our community has evolved across the different “Hack the Hackathon” events. It highlights both new participants joining for the first time and those who have returned to contribute repeatedly, reflecting the strength and continuity of our network.

<section class="py-5 bg-light">
    <div class="container">
        <div id="error_sankey" class="error" style="display: none;"></div>
        <div class="chart-container-sankey">
            <div id="sankey"></div>
            <div class="legend">
                <div class="legend-item">
                    <div class="legend-color" style="background: #4a90e2;"></div>
                    <span>Direct continuation (consecutive events)</span>
                </div>
                <div class="legend-item">
                    <div class="legend-color" style="background: #9b59b6;"></div>
                    <span>First-time participants</span>
                </div>
                <div class="legend-item">
                    <div class="legend-color" style="background: #34c759; border: 2px dashed #34c759; background: transparent;"></div>
                    <span>Returning participants (skipped events)</span>
                </div>
            </div>
        </div>
    </div>
    <div class="tooltip" id="tooltip"></div>
</section>

---

## Our Dedicated Steering Committee {#steering-committee}

Get to know our dedicated steering committee — the group guiding our community between events and helping shape the direction of future “Hack the Hackathon” activities.

If you’d like to get in touch, reach out through our Discord server or send us an email at <a href="mailto:contact@hackthehackathon.org" target="_blank" alt="EMail">contact@hackthehackathon.org</a>.


<section>
    <div class="container steeringcommittee">
        <div class="row text-center">
            <!-- Allissa -->
            <div class="col-md-4">
                <div class="card">
                    <img src="/images/steeringcommittee/allissa.png" class="portrait" alt="Allissa Dillman">
                    <div class="card-body">
                        <h4 class="card-title">Allissa Dillman</h4>
                        <p class="card-text">Social Media Chair</p>
                        <a href="https://www.linkedin.com/in/allissa-dillman/" target="_blank"><i class="fab fa-linkedin"></i></a>
                    </div>
                </div>
            </div>
            <!-- Joseph -->
            <div class="col-md-4">
                <div class="card">
                    <img src="/images/steeringcommittee/joseph.jpg" class="portrait" alt="Joseph Gum">
                    <div class="card-body">
                        <h4 class="card-title">Joseph Gum</h4>
                        <p class="card-text">Secretary</p>
                        <a href="https://www.linkedin.com/in/josephigum/" target="_blank"><i class="fab fa-linkedin"></i></a>
                    </div>
                </div>
            </div>
            <!-- Daniela -->
            <div class="col-md-4">
                <div class="card">
                    <img src="/images/steeringcommittee/daniela.jpg" class="portrait" alt="Daniela Huppenkothen">
                    <div class="card-body">
                        <h4 class="card-title">Daniela Huppenkothen</h4>
                        <p class="card-text">Treasurer</p>
                        <a href="https://www.linkedin.com/in/daniela-h-0b44a97b/" target="_blank"><i class="fab fa-linkedin"></i></a>
                        <a href="https://huppenkothen.org/" target="_blank"><i class="fas fa-globe"></i></a>
                    </div>
                </div>
            </div>
        <div class="row text-center">
        </div>
            <!-- Cecilia -->
            <div class="col-md-4">
                <div class="card">
                    <img src="/images/steeringcommittee/cecilia.jpg" class="portrait" alt="Cecilia La Place">
                    <div class="card-body">
                        <h4 class="card-title">Cecilia La Place</h4>
                        <p class="card-text">Webchair</p>
                        <a href="https://www.linkedin.com/in/cecilia-la-place/" target="_blank"><i class="fab fa-linkedin"></i></a>
                    </div>
                </div>
            </div>
            <!-- Alex -->
            <div class="col-md-4">
                <div class="card">
                    <img src="/images/steeringcommittee/alex.jpg" class="portrait" alt="Alexander Nolte">
                    <div class="card-body">
                        <h4 class="card-title">Alexander Nolte</h4>
                        <p class="card-text">General Chair</p>
                        <a href="https://www.linkedin.com/in/alexandernolte/" target="_blank"><i class="fab fa-linkedin"></i></a>
                        <a href="https://alexandernolte.github.io/" target="_blank"><i class="fas fa-globe"></i></a>
                    </div>
                </div>
            </div>
        </div>
    </div>
</section>



<script> <!-- SCRIPT FOR DOMAINS -->
    const CSV_PATH_RA = '/docs/domains.csv';  
    // Generate colors for each category
    const colors = ['#3b82f6', '#8b5cf6', '#ef4444', '#10b981', '#f59e0b', '#ec4899', '#6366f1', '#84cc16'];
    
    // Function to create muted versions of colors
    function getMutedColor(hexColor, opacity = 0.2) {
        // Convert hex to RGB
        const r = parseInt(hexColor.slice(1, 3), 16);
        const g = parseInt(hexColor.slice(3, 5), 16);
        const b = parseInt(hexColor.slice(5, 7), 16);
        
        // Return as rgba with reduced opacity for muted effect
        return `rgba(${r}, ${g}, ${b}, ${opacity})`;
    }

    let eventsData_domains = [];
    let currentIndex_domains = 0;
    let chart_domains = null;

    function parseCSV_domains(csvText) {
        const lines = csvText.trim().split('\n');
        
        // Function to parse a CSV line properly handling quoted fields
        function parseCSVLine(line) {
            const result = [];
            let current = '';
            let inQuotes = false;
            
            for (let i = 0; i < line.length; i++) {
                const char = line[i];
                
                if (char === '"') {
                    inQuotes = !inQuotes;
                } else if (char === ',' && !inQuotes) {
                    result.push(current.trim());
                    current = '';
                } else {
                    current += char;
                }
            }
            
            result.push(current.trim());
            return result;
        }
        
        const headers = parseCSVLine(lines[0]);
        const eventColumns = headers.slice(1);
        
        // Get all categories from the first column
        const categories = [];
        for (let i = 1; i < lines.length; i++) {
            const values = parseCSVLine(lines[i]);
            const category = values[0];
            if (!categories.includes(category)) {
                categories.push(category);
            }
        }
        
        const data = [];
        eventColumns.forEach(eventName => {
            const eventEntry = { name: eventName, categories: {}, total: 0 };
            
            // Initialize all categories to 0
            categories.forEach(category => {
                eventEntry.categories[category] = 0;
            });
            
            data.push(eventEntry);
        });
        
        // Fill in the data
        for (let i = 1; i < lines.length; i++) {
            const values = parseCSVLine(lines[i]);
            const category = values[0];
            
            eventColumns.forEach((eventName, index) => {
                const value = parseInt(values[index + 1]) || 0;
                const eventEntry = data.find(e => e.name === eventName);
                eventEntry.categories[category] = value;
            });
        }
        
        // Calculate totals
        data.forEach(eventEntry => {
            eventEntry.total = Object.values(eventEntry.categories).reduce((sum, val) => sum + val, 0);
        });
        
        return { events: data, categories: categories };
    }

    function showError_domains(message) {
        const errorDiv = document.getElementById('error');
        errorDiv.textContent = message;
        errorDiv.style.display = 'block';
    }

    function hideError_domains() {
        document.getElementById('error').style.display = 'none';
    }

    function createTimeline_domains() {
        const timeline = document.getElementById('timeline_ra');
        timeline.innerHTML = '';
        
        eventsData_domains.events.forEach((event, index) => {
            const dot = document.createElement('button');
            dot.className = 'timeline-dot';
            if (index === currentIndex_domains) dot.classList.add('active');
            dot.onclick = () => goToEvent_domains(index);
            dot.setAttribute('aria-label', `Go to ${event.name} OP`);
            timeline.appendChild(dot);
            
            if (index < eventsData_domains.events.length - 1) {
                const line = document.createElement('div');
                line.className = 'timeline-line';
                timeline.appendChild(line);
            }
        });
    }

    function updateChart_domains() {
        const event = eventsData_domains.events[currentIndex_domains];
        
        if (chart_domains) {
            chart_domains.destroy();
        }
        
        const ctx = document.getElementById('pieChart_DOMAIN').getContext('2d');
        
        chart_domains = new Chart(ctx, {
            type: 'pie',
            data: {
                labels: eventsData_domains.categories,
                datasets: [{
                    data: eventsData_domains.categories.map(category => event.categories[category]),
                    backgroundColor: colors.slice(0, eventsData_domains.categories.length),
                    borderWidth: 0
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: {
                    legend: {
                        display: false
                    },
                    tooltip: {
                        callbacks: {
                            label: function(context) {
                                const label = context.label || '';
                                const value = context.parsed;
                                const total = context.dataset.data.reduce((a, b) => a + b, 0);
                                const percentage = ((value / total) * 100).toFixed(1);
                                return `${label}: ${value} (${percentage}%)`;
                            }
                        }
                    }
                }
            }
        });
    }

    function updateStats_domains() {
        const event = eventsData_domains.events[currentIndex_domains];
        
        document.getElementById('eventTitle_ra').textContent = event.name;
        
        // Get the stats container for domains
        const statsContainer = document.querySelector('.stats.domains');
        
        // Clear existing category stat cards (keep total)
        const existingCategoryCards = statsContainer.querySelectorAll('.stat-card:not(.total)');
        existingCategoryCards.forEach(card => card.remove());
        
        // Create stat cards dynamically for each category
        const categories = eventsData_domains.categories;
        const totalCard = statsContainer.querySelector('.stat-card.total');
        
        categories.forEach((category, index) => {
            const value = event.categories[category];
            const percentage = event.total > 0 ? ((value / event.total) * 100).toFixed(1) : 0;
            
            // Skip categories with zero values
            if (value === 0) {
                return;
            }
            
            // Create stat card
            const statCard = document.createElement('div');
            statCard.className = `col-md-5 stat-card category-${index}`;
            
            // Get the corresponding muted color from the chart color palette
            const originalColor = colors[index % colors.length];
            const mutedBackgroundColor = getMutedColor(originalColor, 0.15);
            const borderColor = getMutedColor(originalColor, 0.5);
            
            statCard.style.backgroundColor = mutedBackgroundColor;
            statCard.style.border = `2px solid ${borderColor}`;
            statCard.style.color = originalColor; // Use original color for text for good contrast
            
            statCard.innerHTML = `
                <div class="stat-label">${category}</div>
                <div class="stat-percent">${percentage}%</div>
            `;
            
            // Insert before the total card
            statsContainer.insertBefore(statCard, totalCard);
        });
        
        // Update total
        document.getElementById('totalValueDomain').textContent = event.total;
        
        document.getElementById('prevBtn_ra').disabled = currentIndex_domains === 0;
        document.getElementById('nextBtn_ra').disabled = currentIndex_domains === eventsData_domains.events.length - 1;
    }

    function updateDisplay_domains() {
        createTimeline_domains();
        updateChart_domains();
        updateStats_domains();
    }

    function goToEvent_domains(index) {
        currentIndex_domains = index;
        updateDisplay_domains();
    }

    function nextEvent_domains() {
        if (currentIndex_domains < eventsData_domains.events.length - 1) {
            currentIndex_domains++;
            updateDisplay_domains();
        }
    }

    function prevEvent_domains() {
        if (currentIndex_domains > 0) {
            currentIndex_domains--;
            updateDisplay_domains();
        }
    }

    document.getElementById('nextBtn_ra').onclick = nextEvent_domains;
    document.getElementById('prevBtn_ra').onclick = prevEvent_domains;

    // Load data from CSV
    fetch(CSV_PATH_RA)
        .then(response => {
            if (!response.ok) {
                throw new Error(`Could not load CSV file from ${CSV_PATH_RA}. Make sure the file exists and the path is correct.`);
            }
            return response.text();
        })
        .then(csvText => {
            hideError_domains();
            eventsData_domains = parseCSV_domains(csvText);
            if (eventsData_domains.events.length === 0) {
                throw new Error('No data found in CSV file');
            }
            updateDisplay_domains();
        })
        .catch(error => {
            showError_domains(error.message);
            console.error('Error loading data:', error);
        });
</script>

<script> <!-- SCRIPT FOR RESEARCHER V ORGANIZER -->
    const CSV_PATH_OR = '/docs/practitioner_v_researchers.csv';  // Adjust this path for your Nikola setup
    
    // Function to create muted versions of colors
    function getMutedColor_OR(hexColor, opacity = 0.2) {
        // Convert hex to RGB
        const r = parseInt(hexColor.slice(1, 3), 16);
        const g = parseInt(hexColor.slice(3, 5), 16);
        const b = parseInt(hexColor.slice(5, 7), 16);
        
        // Return as rgba with reduced opacity for muted effect
        return `rgba(${r}, ${g}, ${b}, ${opacity})`;
    }

    let eventsData_practitioner_organizer = [];
    let currentIndex_practitioner_organizer = 0;
    let chart_practitioner_organizer = null;

    function parseCSV_practitioner_organizer(csvText) {
        const lines = csvText.trim().split('\n');
        const headers = lines[0].split(',').map(h => h.trim());
        const eventColumns = headers.slice(1);
        
        const data = [];
        for (let i = 1; i < lines.length; i++) {
            const values = lines[i].split(',').map(v => v.trim());
            const position = values[0];
            
            eventColumns.forEach((eventName, index) => {
                const value = parseInt(values[index + 1]) || 0;
                
                let eventEntry = data.find(e => e.name === eventName);
                if (!eventEntry) {
                    eventEntry = { name: eventName, practitioners: 0, researchers: 0, total: 0 };
                    data.push(eventEntry);
                }
                
                if (position.toLowerCase().includes('practitioner')) {
                    eventEntry.practitioners = value;
                } else if (position.toLowerCase().includes('researcher')) {
                    eventEntry.researchers = value;
                }
                eventEntry.total = eventEntry.practitioners + eventEntry.researchers;
            });
        }
        
        return data;
    }

    function showError_practitioner_organizer(message) {
        const errorDiv = document.getElementById('error');
        errorDiv.textContent = message;
        errorDiv.style.display = 'block';
    }

    function hideError_practitioner_organizer() {
        document.getElementById('error').style.display = 'none';
    }

    function createTimeline_practitioner_organizer() {
        const timeline = document.getElementById('timeline_or');
        timeline.innerHTML = '';
        
        eventsData_practitioner_organizer.forEach((event, index) => {
            const dot = document.createElement('button');
            dot.className = 'timeline-dot';
            if (index === currentIndex_practitioner_organizer) dot.classList.add('active');
            dot.onclick = () => goToEvent_practitioner_organizer(index);
            dot.setAttribute('aria-label', `Go to ${event.name} OP`);
            timeline.appendChild(dot);
            
            if (index < eventsData_practitioner_organizer.length - 1) {
                const line = document.createElement('div');
                line.className = 'timeline-line';
                timeline.appendChild(line);
            }
        });
    }

    function updateChart_practitioner_organizer() {
        const event = eventsData_practitioner_organizer[currentIndex_practitioner_organizer];
        
        if (chart_practitioner_organizer) {
            chart_practitioner_organizer.destroy();
        }
        
        const ctx = document.getElementById('pieChart_RO').getContext('2d');
        chart_practitioner_organizer = new Chart(ctx, {
            type: 'pie',
            data: {
                labels: ['Practitioners', 'Researchers'],
                datasets: [{
                    data: [event.practitioners, event.researchers],
                    backgroundColor: ['#3b82f6', '#8b5cf6'],
                    borderWidth: 0
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: {
                    legend: {
                        display: false
                    },
                    tooltip: {
                        callbacks: {
                            label: function(context) {
                                const label = context.label || '';
                                const value = context.parsed;
                                const total = context.dataset.data.reduce((a, b) => a + b, 0);
                                const percentage = ((value / total) * 100).toFixed(1);
                                return `${label}: ${value} (${percentage}%)`;
                            }
                        }
                    }
                }
            }
        });
    }

    function updateStats_practitioner_organizer() {
        const event = eventsData_practitioner_organizer[currentIndex_practitioner_organizer];
        
        document.getElementById('eventTitle_or').textContent = event.name;
        
        // Apply muted colors to practitioner card
        const practitionerCard = document.querySelector('.stat-card.practitioners');
        const practitionerColor = '#3b82f6'; // Blue
        practitionerCard.style.backgroundColor = getMutedColor_OR(practitionerColor, 0.15);
        practitionerCard.style.border = `2px solid ${getMutedColor_OR(practitionerColor, 0.5)}`;
        practitionerCard.style.color = practitionerColor;
        
        // Apply muted colors to researcher card
        const researcherCard = document.querySelector('.stat-card.researchers');
        const researcherColor = '#8b5cf6'; // Purple
        researcherCard.style.backgroundColor = getMutedColor_OR(researcherColor, 0.15);
        researcherCard.style.border = `2px solid ${getMutedColor_OR(researcherColor, 0.5)}`;
        researcherCard.style.color = researcherColor;
        
        document.getElementById('practitionerPercent').textContent = 
            `${((event.practitioners / event.total) * 100).toFixed(1)}%`;
        
        document.getElementById('researcherPercent').textContent = 
            `${((event.researchers / event.total) * 100).toFixed(1)}%`;
        
        document.getElementById('totalValue').textContent = event.total;
        
        document.getElementById('prevBtn_or').disabled = currentIndex_practitioner_organizer === 0;
        document.getElementById('nextBtn_or').disabled = currentIndex_practitioner_organizer === eventsData_practitioner_organizer.length - 1;
    }

    function updateDisplay_practitioner_organizer() {
        createTimeline_practitioner_organizer();
        updateChart_practitioner_organizer();
        updateStats_practitioner_organizer();
    }

    function goToEvent_practitioner_organizer(index) {
        currentIndex_practitioner_organizer = index;
        updateDisplay_practitioner_organizer();
    }

    function nextEvent_practitioner_organizer() {
        if (currentIndex_practitioner_organizer < eventsData_practitioner_organizer.length - 1) {
            currentIndex_practitioner_organizer++;
            updateDisplay_practitioner_organizer();
        }
    }

    function prevEvent_practitioner_organizer() {
        if (currentIndex_practitioner_organizer > 0) {
            currentIndex_practitioner_organizer--;
            updateDisplay_practitioner_organizer();
        }
    }

    document.getElementById('nextBtn_or').onclick = nextEvent_practitioner_organizer;
    document.getElementById('prevBtn_or').onclick = prevEvent_practitioner_organizer;

    // Load data from CSV
    fetch(CSV_PATH_OR)
        .then(response => {
            if (!response.ok) {
                throw new Error(`Could not load CSV file from ${CSV_PATH_OR}. Make sure the file exists and the path is correct.`);
            }
            return response.text();
        })
        .then(csvText => {
            hideError_practitioner_organizer();
            eventsData_practitioner_organizer = parseCSV_practitioner_organizer(csvText);
            if (eventsData_practitioner_organizer.length === 0) {
                throw new Error('No data found in CSV file');
            }
            updateDisplay_practitioner_organizer();
        })
        .catch(error => {
            showError_practitioner_organizer(error.message);
            console.error('Error loading data:', error);
        });
</script>

<script> <!-- SCRIPT FOR CONTINUED PARTICIPATION -->
    // CONFIGURATION: Change this path to where your CSV file is located
    const CSV_PATH = '/docs/continued_participation.csv';

    function parseParticipantCSV(csvText) {
        const lines = csvText.trim().split('\n');
        const headers = lines[0].split(',').map(h => h.trim());
        
        const participants = [];
        for (let i = 1; i < lines.length; i++) {
            const values = lines[i].split(',').map(v => v.trim().toLowerCase());
            const attendance = {};
            headers.forEach((event, index) => {
                attendance[event] = values[index] === 'yes';
            });
            participants.push(attendance);
        }
        
        return { headers, participants };
    }

    function calculateRetentionStats(headers, participants) {
        const stats = {};
        
        headers.forEach(event => {
            const attended = participants.filter(p => p[event]).length;
            stats[event] = {
                total: attended,
                percentage: (attended / participants.length * 100).toFixed(1)
            };
        });
        
        return stats;
    }

    function createSankeyData(headers, participants) {
        const nodes = [];
        const links = [];
        let nodeId = 0;
        
        // Create event nodes
        headers.forEach((event, index) => {
            nodes.push({ 
                name: event,
                id: nodeId++,
                type: 'event',
                color: '#4a90e2',
                eventIndex: index
            });
        });
        
        // Add single newcomer source node
        nodes.push({
            name: `Newcomers`,
            id: nodeId++,
            type: 'newcomers',
            color: '#9b59b6'
        });
        
        // Calculate participant flows
        for (let i = 0; i < headers.length; i++) {
            const currentEvent = headers[i];
            const currentEventNode = nodes.find(n => n.name === currentEvent && n.type === 'event');
            
            if (i === 0) {
                // First event: all participants are newcomers
                const currentAttendees = participants.filter(p => p[currentEvent]);
                const newcomerNode = nodes.find(n => n.type === 'newcomers');
                links.push({
                    source: newcomerNode.id,
                    target: currentEventNode.id,
                    value: currentAttendees.length,
                    type: 'newcomers'
                });
            } else {
                // For subsequent events, track where each participant came from
                const currentEventParticipants = participants.filter(p => p[currentEvent]);
                
                // Group participants by their most recent previous event attendance
                const participantFlows = new Map();
                
                currentEventParticipants.forEach(participant => {
                    // Find the most recent event this participant attended before current event
                    let mostRecentEventIndex = -1;
                    for (let j = i - 1; j >= 0; j--) {
                        if (participant[headers[j]]) {
                            mostRecentEventIndex = j;
                            break;
                        }
                    }
                    
                    const flowKey = mostRecentEventIndex >= 0 ? `event_${mostRecentEventIndex}` : 'newcomer';
                    participantFlows.set(flowKey, (participantFlows.get(flowKey) || 0) + 1);
                });
                
                // Create flows based on participant sources
                participantFlows.forEach((count, flowKey) => {
                    if (flowKey === 'newcomer') {
                        // True newcomer flow from single newcomer node
                        const newcomerNode = nodes.find(n => n.type === 'newcomers');
                        links.push({
                            source: newcomerNode.id,
                            target: currentEventNode.id,
                            value: count,
                            type: 'newcomers'
                        });
                    } else {
                        // Returning participant flow from their most recent event
                        const sourceEventIndex = parseInt(flowKey.split('_')[1]);
                        const sourceEventNode = nodes.find(n => n.type === 'event' && n.eventIndex === sourceEventIndex);
                        
                        const isDirectContinuation = sourceEventIndex === i - 1;
                        const gapSize = i - sourceEventIndex - 1;
                        
                        links.push({
                            source: sourceEventNode.id,
                            target: currentEventNode.id,
                            value: count,
                            type: isDirectContinuation ? 'direct_continuation' : 'returning_jump',
                            gap: gapSize,
                            sourceEventName: headers[sourceEventIndex],
                            targetEventName: headers[i]
                        });
                    }
                });
                
                // Calculate retention rate from immediate previous event for display
                const previousEvent = headers[i - 1];
                const previousEventNode = nodes.find(n => n.name === previousEvent && n.type === 'event');
                const previousAttendees = participants.filter(p => p[previousEvent]);
                const directContinuing = participants.filter(p => p[previousEvent] && p[currentEvent]).length;
                
                if (previousAttendees.length > 0 && directContinuing > 0) {
                    const retentionRate = Math.round((directContinuing / previousAttendees.length) * 100);
                    
                    // Find the direct continuation link and add retention rate
                    const directLink = links.find(l => 
                        l.source === previousEventNode.id && 
                        l.target === currentEventNode.id && 
                        l.type === 'direct_continuation'
                    );
                    if (directLink) {
                        directLink.retentionRate = retentionRate;
                    }
                }
            }
        }
        
        return { nodes, links };
    }

    function drawSankey(data) {
        // Alphanumeric sort function for node names (reversed order)
        function alphanumericSortReverse(a, b) {
            // Extract the name for comparison
            const nameA = a.name || '';
            const nameB = b.name || '';
            
            // Split into segments of letters and numbers
            const segmentA = nameA.match(/(\d+|\D+)/g) || [];
            const segmentB = nameB.match(/(\d+|\D+)/g) || [];
            
            const maxLength = Math.max(segmentA.length, segmentB.length);
            
            for (let i = 0; i < maxLength; i++) {
                const partA = segmentA[i] || '';
                const partB = segmentB[i] || '';
                
                // Check if both parts are numeric
                const numA = parseInt(partA, 10);
                const numB = parseInt(partB, 10);
                
                if (!isNaN(numA) && !isNaN(numB)) {
                    // Both are numbers - compare numerically (reversed)
                    if (numA !== numB) {
                        return -(numB - numA); // Reversed order
                    }
                } else {
                    // At least one is text - compare as strings (reversed)
                    const comparison = partB.localeCompare(partA, undefined, { 
                        numeric: true, 
                        sensitivity: 'base' 
                    });
                    if (comparison !== 0) {
                        return -comparison;
                    }
                }
            }
            
            return 0;
        }
        
        const container = document.getElementById('sankey');
        
        // Ensure container has proper dimensions
        const width = Math.max(container.clientWidth, 800); // Increased minimum width
        const height = Math.max(container.clientHeight, 500); // Increased minimum height
        
        // If container still has no dimensions, set them explicitly
        if (container.clientWidth === 0) {
            container.style.width = '100%';
            container.style.height = '500px';
        }
        
        // Clear previous
        d3.select('#sankey').selectAll('*').remove();
        
        const svg = d3.select('#sankey')
            .append('svg')
            .attr('width', width)
            .attr('height', height);
        
        // Validate that we have valid dimensions before proceeding
        if (width <= 80 || height <= 40) {
            console.error('Container dimensions too small for Sankey diagram');
            return;
        }
        
        const sankey = d3.sankey()
            .nodeWidth(20)
            .nodePadding(30)
            .extent([[50, 30], [width - 50, height - 50]])
            .nodeSort(null); // Disable automatic sorting since we sort manually
        
        // Validate data before processing
        if (!data.nodes || !data.links || data.nodes.length === 0) {
            console.error('Invalid or empty Sankey data');
            return;
        }
        
        // Manually sort nodes before passing to Sankey (reverse alphanumeric order)
        const sortedNodes = data.nodes.map(d => Object.assign({}, d)).sort(alphanumericSortReverse);
        
        const { nodes, links } = sankey({
            nodes: sortedNodes,
            links: data.links.map(d => Object.assign({}, d))
        });

        // Manually adjust outgoing flow positions: direct continuation first, then returning jumps
        nodes.forEach(node => {
            // Only adjust outgoing flows (sourceLinks)
            const outgoingLinks = node.sourceLinks || [];
            
            // Sort outgoing links: direct_continuation first, then newcomers, then returning_jump last
            const sortedOutgoingLinks = outgoingLinks.sort((a, b) => {
                const priorityOrder = { 'direct_continuation': 0, 'newcomers': 1, 'returning_jump': 2 };
                return (priorityOrder[a.type] || 3) - (priorityOrder[b.type] || 3);
            });
            
            // Recalculate outgoing flow positions
            let currentY = node.y0;
            sortedOutgoingLinks.forEach(link => {
                link.sy0 = currentY;
                link.sy1 = currentY + link.width;
                currentY += link.width;
                
                // Update the vertical position of the flow
                link.y0 = (link.sy0 + link.sy1) / 2;
            });
        });

        const tooltip = d3.select('#tooltip');
        
        // Define colors for different flow types
        const colors = {
            direct_continuation: '#4a90e2',
            returning_jump: '#34c759',
            newcomers: '#9b59b6',
            event: '#2c5aa0'
        };
        
        // Draw links with custom styling
        svg.append('g')
            .selectAll('path')
            .data(links)
            .enter()
            .append('path')
            .attr('class', 'link')
            .attr('d', d3.sankeyLinkHorizontal())
            .attr('stroke', d => {
                if (d.type === 'newcomers') return colors.newcomers;
                if (d.type === 'returning_jump') return colors.returning_jump;
                if (d.type === 'direct_continuation') return colors.direct_continuation;
                return colors.direct_continuation;
            })
            .attr('stroke-width', d => Math.max(2, d.width))
            .attr('fill', 'none')
            .attr('opacity', d => {
                if (d.type === 'returning_jump') return 0.7; // More visible for jumps
                return 0.6;
            })
            .attr('stroke-dasharray', d => {
                if (d.type === 'returning_jump') {
                    // Longer dashes for bigger jumps
                    const dashLength = Math.min(10, 5 + d.gap * 2);
                    return `${dashLength},${dashLength}`;
                }
                return 'none';
            })
            .on('mouseover', function(event, d) {
                const sourceNode = d.source.name;
                const targetNode = d.target.name;
                let tooltipText = `<strong>${sourceNode}</strong> → <strong>${targetNode}</strong><br/>${d.value} participant${d.value !== 1 ? 's' : ''}`;
                
                if (d.retentionRate) {
                    tooltipText += `<br/>Direct retention rate: ${d.retentionRate}%`;
                }
                if (d.type === 'returning_jump') {
                    const skippedEvents = d.gap;
                    if (skippedEvents === 1) {
                        tooltipText += `<br/>Skipped 1 event`;
                    } else if (skippedEvents > 1) {
                        tooltipText += `<br/>Skipped ${skippedEvents} events`;
                    }
                }
                if (d.type === 'newcomers') {
                    tooltipText += `<br/>First-time participants`;
                }
                
                tooltip.style('opacity', 1).html(tooltipText);
            })
            .on('mousemove', function(event) {
                tooltip.style('left', (event.pageX + 20) + 'px')
                    .style('top', (event.pageY - 20) + 'px');
            })
            .on('mouseout', function() {
                tooltip.style('opacity', 0);
            });
        
        // Draw nodes
        const node = svg.append('g')
            .selectAll('g')
            .data(nodes)
            .enter()
            .append('g')
            .attr('class', 'node');
        
        node.append('rect')
            .attr('x', d => d.x0)
            .attr('y', d => d.y0)
            .attr('height', d => d.y1 - d.y0)
            .attr('width', d => d.x1 - d.x0)
            .attr('fill', d => {
                if (d.type === 'newcomers') return colors.newcomers;
                if (d.type === 'event') return colors.event;
                return d.color;
            })
            .attr('rx', 3)
            .on('mouseover', function(event, d) {
                const inflow = d.targetLinks.reduce((sum, l) => sum + l.value, 0);
                const outflow = d.sourceLinks.reduce((sum, l) => sum + l.value, 0);
                let tooltipText = `<strong>${d.name}</strong><br/>Participants: ${Math.max(inflow, outflow)}`;
                if (d.type === 'newcomers') {
                    tooltipText += `<br/>First-time participants only`;
                } else if (d.type === 'event') {
                    tooltipText += `<br/>Total event attendance`;
                }
                tooltip.style('opacity', 1).html(tooltipText);
            })
            .on('mousemove', function(event) {
                tooltip.style('left', (event.pageX + 10) + 'px')
                    .style('top', (event.pageY - 10) + 'px');
            })
            .on('mouseout', function() {
                tooltip.style('opacity', 0);
            });
        
        // Add labels with better positioning
        node.append('text')
            .attr('x', d => {
                if (d.type === 'newcomers') {
                    return d.x1 + 10; // Right of newcomer nodes
                } else {
                    return d.x1 + 10; // Right of event nodes
                }
            })
            .attr('y', d => (d.y1 + d.y0) / 2)
            .attr('dy', '0.35em')
            .attr('text-anchor', 'start') // Always align text to start since all labels are now on the right
            .text(d => d.name)
            .style('fill', '#1e293b')
            .style('font-weight', d => d.type === 'event' ? 'bold' : 'normal')
            .style('font-size', '14px');
        
        // Add retention percentage labels on links
        svg.append('g')
            .selectAll('text')
            .data(links.filter(d => d.retentionRate))
            .enter()
            .append('text')
            .attr('x', d => (d.source.x1 + d.target.x0) / 2)
            .attr('y', d => (d.y0 + d.y1) / 2)
            .attr('dy', '0.35em')
            .attr('text-anchor', 'middle')
            .style('fill', '#1e293b')
            .style('font-weight', 'bold')
            .style('font-size', '12px')
            .style('background', 'white')
            .text(d => `${d.retentionRate}%`);
    }    function showError(message) {
        const errorDiv = document.getElementById('error_sankey');
        errorDiv.textContent = message;
        errorDiv.style.display = 'block';
    }

    function hideError() {
        document.getElementById('error_sankey').style.display = 'none';
    }

    // Load and process data
    fetch(CSV_PATH)
        .then(response => {
            if (!response.ok) {
                throw new Error(`Could not load CSV file from ${CSV_PATH}. Make sure the file exists and the path is correct.`);
            }
            return response.text();
        })
        .then(csvText => {
            hideError();
            const { headers, participants } = parseParticipantCSV(csvText);
            const stats = calculateRetentionStats(headers, participants);
            const sankeyData = createSankeyData(headers, participants);
            
            drawSankey(sankeyData);
            
            // Redraw on resize
            window.addEventListener('resize', () => {
                drawSankey(sankeyData);
            });
        })
        .catch(error => {
            showError(error.message);
            console.error('Error loading data:', error);
        });
</script>
