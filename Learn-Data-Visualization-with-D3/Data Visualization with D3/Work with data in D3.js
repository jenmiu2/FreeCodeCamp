<body>
  <script>
    const dataset = [12, 31, 22, 17, 25, 18, 29, 14, 9];

    // Add your code below this line
    const anchor = d3.select("body")
                     .selectAll()
                     .data(dataset)
                     .enter()
                     .append("h2")
                     .text("New Title")


    // Add your code above this line
  </script>
</body>
