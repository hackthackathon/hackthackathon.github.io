<!--
.. title: Resources
.. slug: resources
.. hide_title: false
.. date: 2024-11-21 19:32:05 UTC
.. tags: 
.. category: 
.. link: 
.. description: 
.. type: text
-->

# Resources

<table id="resources" class="display" style="width:100%">
  <thead>
    <tr>
      <th>Author/Creator</th>
      <th>Title</th>
      <th>Type</th>
      <th>Where to find</th>
    </tr>
  </thead>
  <tbody>

  </tbody>
</table>

<!-- Clear Filter Button -->
  <button class="clear-filter" onclick="clearTagFilter()">Clear Filter</button>


<!-- Include DataTables.js -->
<script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
<script src="https://cdn.datatables.net/1.13.1/js/jquery.dataTables.min.js"></script>
<link rel="stylesheet" href="https://cdn.datatables.net/1.13.1/css/jquery.dataTables.min.css">

<script>
    var newJQuery = jQuery.noConflict(true); 
    newJQuery(document).ready(function() {
        const table = newJQuery('#resources').DataTable({
            paging: true,
            searching: true,
            ordering: true,
            info: true,
            autoWidth: true
        }); 

        function loadCSVData(url) {
            newJQuery.get(url, function (data) {
                const rows = parseCSV(data);
                rows.shift(); 
                rows.forEach(cols => {                    
                    const types = cols[4].split(",").map(type => {
                        const tag = `<span class="tag ${type.trim().replace(/\s+/g, '-').toLowerCase()}" onclick="applyTagFilter('${type.trim()}')">${type.trim()}</span>`;
                        return tag;
                    }).join(" "); 

                    table.row.add([
                    cols[2],  
                    cols[3], 
                    types,
                    cols[5] ? `<a href="${cols[5]}">LINK</a>` : "",
                    ]).draw();
                });
                table.columns.adjust();
            });
        }

        
        function parseCSV(csvText) {
            const rows = [];
            const regex = /(?:^|,)(?:"([^"]*(?:""[^"]*)*)"|([^",]*))/g;
            
            csvText.split('\n').forEach(line => {
                const matches = [];
                let match;
                while ((match = regex.exec(line)) !== null) {
                    const value = match[1] || match[2] || ""; 
                    matches.push(value.replace(/""/g, '"').trim()); 
                }
                if (matches.length > 1 || matches[0] !== "") rows.push(matches); 
            });
            
            return rows;
        }

        loadCSVData("/docs/resources.csv");
    
        window.applyTagFilter = function (tagText) {
            newJQuery('.tag').removeClass('active-tag'); 
            newJQuery(`.tag:contains(${tagText})`).addClass('active-tag'); 
            
            table.search(tagText).draw();
        };
    
        window.clearTagFilter = function () {
            table.search('').draw(); 
            newJQuery('.tag').removeClass('active-tag'); 
        };
    });
</script>
