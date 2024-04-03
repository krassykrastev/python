function solve() {
   document.querySelector('#searchBtn').addEventListener('click', onClick);

   function onClick() {
      const trElements = Array.from(document.querySelectorAll('table.container tbody tr'));
      const searchFieldElement = document.querySelector('#searchField');
      const searchText = searchFieldElement.value.toLowerCase();
      
      for (const trElement of trElements) {
         const tdElements = trElement.querySelectorAll('td');
         let isSelected = false;
         trElement.classList.remove('select');

         for (const tdElement of tdElements) {
            if (tdElement.textContent.toLowerCase().includes(searchText)) {
               isSelected = true;
               break;
            }
         }
         if (isSelected) {
            trElement.classList.add('select');
         }
      }
      searchFieldElement.value = '';
   }
}