import json
import os
from nikola.plugin_categories import ShortcodePlugin

class GalleryCarousel(ShortcodePlugin):
    name = "gallery_carousel"

    def handler(self, data_file, carousel_id="myCarousel", site=None, data=None, lang=None, post=None):
        # Make path relative to site root if needed
        if not os.path.isabs(data_file):
            data_file = os.path.join(site.config['OUTPUT_FOLDER'], '..', data_file)
        
        # Read JSON file
        with open(data_file, 'r') as f:
            gallery_data = json.load(f)
        
        images = gallery_data.get('images', [])
        
        # Generate indicators
        indicators_html = '<ol class="carousel-indicators">'
        for i in range(len(images)):
            active = ' class="active"' if i == 0 else ''
            indicators_html += f'<li data-target="#{carousel_id}" data-slide-to="{i}"{active}></li>'
        indicators_html += '</ol>'
        
        # Generate carousel items
        items_html = '<div class="carousel-inner" role="listbox">'
        for i, img in enumerate(images):
            active = ' active' if i == 0 else ''
            items_html += f'<div class="item{active}">'
            items_html += f'<img src="{img["src"]}" alt="{img.get("alt", "")}">'
            
            if img.get('title') or img.get('description'):
                items_html += '<div class="carousel-caption">'
                if img.get('title'):
                    items_html += f'<h3>{img["title"]}</h3>'
                if img.get('description'):
                    items_html += f'<p>{img["description"]}</p>'
                items_html += '</div>'
            
            items_html += '</div>'
        items_html += '</div>'
        
        # Generate complete carousel
        html = f'''
        <div id="{carousel_id}" class="carousel slide" data-ride="carousel" data-interval="false">
          {indicators_html}
          {items_html}
          <a class="left carousel-control" href="#{carousel_id}" role="button" data-slide="prev">
            <span class="glyphicon glyphicon-chevron-left" aria-hidden="true"></span>
            <span class="sr-only">Previous</span>
          </a>
          <a class="right carousel-control" href="#{carousel_id}" role="button" data-slide="next">
            <span class="glyphicon glyphicon-chevron-right" aria-hidden="true"></span>
            <span class="sr-only">Next</span>
          </a>
        </div>
        <script>
        $(document).ready(function() {{
          var carousel = $('#{carousel_id}');
          var startX = 0;
          carousel.on('touchstart', function(e) {{
            startX = e.originalEvent.touches[0].pageX;
          }});
          carousel.on('touchend', function(e) {{
            var endX = e.originalEvent.changedTouches[0].pageX;
            if (startX - endX > 50) {{
              carousel.carousel('next');
            }} else if (endX - startX > 50) {{
              carousel.carousel('prev');
            }}
          }});
        }});
        </script>
        '''
        
        return html, []
