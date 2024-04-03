function search() {
   const townListElement = document.getElementById('towns');
   const searchTextElement = document.getElementById('searchText').value;
   const resultElement = document.getElementById('result');
   const townElements = Array.from(townListElement.children);
   let matchCount = 0;

   for (const townElement of townElements) {
      if (townElement.textContent.toLowerCase().includes(searchTextElement.toLowerCase())) {
         townElement.style.fontWeight = 'bold';
         townElement.style.textDecoration = 'underline';
         matchCount++;
      }
   }
   resultElement.textContent = `${matchCount} matches found`;
}