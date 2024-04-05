function solve() {
   const addProductButtonsElements = document.querySelectorAll('button.add-product');
   const textAreaElement = document.querySelector('textarea');
   const checkOutButtonElement = document.querySelector('button.checkout');
   let totalPrice = 0;
   let uniqueProducts = {};
   
   for (const buttonElement of addProductButtonsElements) {
      const productElement = buttonElement.parentElement.parentElement;

      buttonElement.addEventListener('click', () => {
         const title = productElement.querySelector('.product-title').textContent;
         const price = Number(productElement.querySelector('.product-line-price').textContent);
         totalPrice += price;
         uniqueProducts[title] = true;

         textAreaElement.textContent += `Added ${title} for ${price.toFixed(2)} to the cart.\n`;
      });
   }
   checkOutButtonElement.addEventListener('click', (event) => {
      Array.from(addProductButtonsElements).forEach(buttonElement => buttonElement.disabled = true);
      event.target.disabled = true;
      const list = Object.keys(uniqueProducts).join(', ');

      textAreaElement.textContent += `You bought ${list} for ${totalPrice.toFixed(2)}.`;
   });
}