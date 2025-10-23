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

This page gathers a wide array of resources both from our community and the wider field of hackathon research. We also include tools, software, artifacts and planning kids from our workshops and beyond. If you'd like to browse all of the available resources, go to [all resources](#all-resources). Below, we will highlight a few resources you might be particularly interested in.

## Getting Started

If you're just getting started with hackathons, you might be interested in one of the several planning kits and start-up resources we have developed. Some highlights to get you started include:

 - The [Hackathon Planning Kit](https://hackathon-planning-kit.org) provides you with example timelines, decision guides and tons of resources to jump-start your hackathon organization. 
 - How do you know whether your hackathon worked, and whether it was a good experience for participants? Check out this [survey](https://zenodo.org/records/14705828) to get you started with evaluating your event.
 - Setting up the technical side of hackathons can be challenging. To help set you up, one team at Hack the Hackathon developed a hackathon cookiecutter template that sets you up with a website and more! Check out the [Hackathon Cookiecutter Template](https://github.com/hackthackathon/hackathon-template-cookiecutter). 

## Recent Academic Highlights

There is a thriving community researching all facets of human collaboration and interaction at hackathons. These results are fascinating in their own right, but also provide valuable insights to organizers to help improve the participant experience. Here are three recent highlights from our community:

 - What are hackathons? Where are we as a field, and what is the future of hackathons? [The Future of Hackathon Research and Practice (Falk et al, 2025)](https://ieeexplore.ieee.org/document/10666667) sets out to answer these questions and more. Born out of initial discussions at Hack the Hackathon 1, this paper includes the perspectives of a wide range of researchers and practitioners.  
 - What is the role of hackathons as a venue for learning? A recent literature study, [How do we learn in and from Hackathons? A systematic literature review (Schulten + Chounta, 2024)](https://link.springer.com/article/10.1007/s10639-024-12668-1), will tell you more. 
 - What role do hackathons play in academic research? Where and how are they used? [10 Years of Research With and On Hackathons (Falk + Halskov (2020))](https://dl.acm.org/doi/10.1145/3357236.3395543) surveyed the available literature and explored motivations for research with and about hackathons.  
 - How do we know whether a hackathon was successful? What does success even mean? [What Do We Know About Hackathon Outcomes and How to Support Them? – A Systematic Literature Review (Medina Angarita + Nolte (2020))](https://hackathon-planning-kit.org/files/Medina-Collabtech-2020.pdf) report on the state-of-the-art of potential hackathon outcomes, design aspects and connections between them.


## All Resources {#all-resources}
Take a look at the sortable table below to explore the breadth and width of resources. They include academic papers, books, tools, planning kits and more!

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
