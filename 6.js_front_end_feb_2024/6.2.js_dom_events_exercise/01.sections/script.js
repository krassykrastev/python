function create(words) {
   const contentElement = document.getElementById('content');
   
   //create div with paragraph
   const divElements = words
      .map(word => {
         //create paragraph
         const pElement = document.createElement('p');
         
         //add text content
         pElement.textContent = word;
         
         //hide the paragraph
         pElement.style.display = 'none';

         //create div
         const divElement = document.createElement('div');

         //append paragraph to div
         divElement.appendChild(pElement);

         //show paragraph on div click
         divElement.addEventListener('click', () => {
            pElement.style.display = 'block';
         });

         //return div
         return divElement;
      });


   //append all to dom
   divElements.forEach(divElement => contentElement.appendChild(divElement));
}