---
layout: page
title: REST API & Tableau
nav-menu: true
image: assets/images/pic05.jpg
---

<!-- Main -->
<div id="main" class="alt">

<!-- One -->
<section id="one">
	<div class="inner">
		<header class="major">
			<h1>UF Organization Chart</h1>
		</header>

<!-- Content -->
<h2 id="content">Using Discogs API to populate images into Tableau</h2>
<p> The primary purpose of this project was to convert my Discogs library into a n interactive Tableau dashboard with graphics. I also did not want to have to download each album artwork manually so I wrote a 
<a href="https://github.com/41-14/41-14.github.io/blob/master/AlbumArtGet.py">script</a> to use Discogs API to download album artwork for my library. </p>
<p>In order to achieve this I first exported my collection to csv. Using pandas, I loaded the csv as a df. I then cast the column which contained the ids per album to a list. I iterated through that list to call a download of each album artwork image. I then created a dashboard in tableau around this idea.</p>
<div class='tableauPlaceholder' id='viz1592842696722' style='position: relative'><noscript><a href='#'><img alt=' ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;vi&#47;vinylcollection&#47;Sheet1&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='vinylcollection&#47;Sheet1' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;vi&#47;vinylcollection&#47;Sheet1&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en' /><param name='filter' value='publish=yes' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1592842696722');                    var vizElement = divElement.getElementsByTagName('object')[0];                    vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';                    var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>
</div>