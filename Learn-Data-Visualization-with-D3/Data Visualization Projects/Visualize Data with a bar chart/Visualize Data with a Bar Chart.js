<script>
 document.addEventListener('DOMContentLoaded',function(){
    document.getElementById('getMessage').onclick= () => {
      
    fetch('https://raw.githubusercontent.com/freeCodeCamp/ProjectReferenceData/master/GDP-data.json')
	.then(response => response.json())
	.then(data => {
		document.getElementById('data').innertHTML = JSON.stringify(data);
	});

      
    };
  });
	
</script>
