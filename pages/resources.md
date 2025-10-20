<!--
.. title: Resources
.. slug: resources
.. hide_title: false
.. date: 2024-11-21 19:32:11 UTC
.. tags: 
.. category: 
.. link: 
.. description: 
.. type: text
-->

<table id="resources" class="display" style="width:100%">
  <thead>
    <tr>
      <th>Author/Creator</th>
      <th>Added by</th>
      <th>Title</th>
      <th>Type</th>
      <th>Where to find</th>
      <th>Resources right here</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Author A and Author B</td>
      <td>ME</td>
      <td>Fascinating Title 1</td>
      <td>
        <span class="tag article" onclick="applyTagFilter('article')">article</span>
      </td>
      <td><a href="link-to-journal">link-to-journal</a></td>
      <td></td>
    </tr>
    <tr>
      <td>Organization X</td>
      <td>ME</td>
      <td>Framework xyz</td>
      <td>
        <span class="tag framework" onclick="applyTagFilter('framework')">framework</span>
        <span class="tag organize" onclick="applyTagFilter('how to organize')">how to organize</span>
      </td>
      <td></td>
      <td><a href="pdf-link-on-website">pdf-link-on-website</a></td>
    </tr>
    <tr>
      <td>Author B and Author C</td>
      <td>XYZ</td>
      <td>Another great title</td>
      <td>
        <span class="tag article" onclick="applyTagFilter('article')">article</span>
        <span class="tag organize" onclick="applyTagFilter('how to organize')">how to organize</span>
      </td>
      <td><a href="link-to-xarchive">link-to-xarchive</a></td>
      <td></td>
    </tr>
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
      info: true
    });
    
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
