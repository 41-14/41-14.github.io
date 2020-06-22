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
<p>The following dashboard is a simplified demo version of IPR's UF Organization Chart recreated in Tableau. The primary goal was to allow for more information to be stored in one file rather than having to use multiple image files. Other benefits include the ability to store information such as emails and phone numbers in tooltips and being able to update a value in a table and getting new information out rather than recreating a set of images. Orange bars indicate completed pathing, while blue shows data objects that could be completed in a future final version. It currently is structured as bars, but by assigning x,y coordinates to my table file it could be easily converted back to a chart. </p>
<p>To use simply mouse over to see more information and click on a bar to drill down a tier.</p>
<iframe seamless frameborder="0" src="https://public.tableau.com/views/vinylcollection/Sheet1??:embed=yes&:display_count=yes&:showVizHome=no" width = '1050' height = '850' scrolling='yes' ></iframe>
<div class='tableauPlaceholder' id='viz1592842696722' style='position: relative'><noscript><a href='#'><img alt=' ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;vi&#47;vinylcollection&#47;Sheet1&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='vinylcollection&#47;Sheet1' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;vi&#47;vinylcollection&#47;Sheet1&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en' /><param name='filter' value='publish=yes' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1592842696722');                    var vizElement = divElement.getElementsByTagName('object')[0];                    vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';                    var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>
</div>