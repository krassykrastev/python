function encodeAndDecodeMessages() {
    const firstTextBoxElement = document.querySelector('#main div:nth-child(1) textarea');
    const firstTextButtonElement = document.querySelector('#main div:nth-child(1) button');

    const secondTextBoxElement = document.querySelector('#main div:nth-child(2) textarea');
    const secondTextButtonElement = document.querySelector('#main div:nth-child(2) button');

    firstTextButtonElement.addEventListener('click', () => {
        const originalText = firstTextBoxElement.value;
        firstTextBoxElement.value = '';
        secondTextBoxElement.value = shiftString(originalText, true);
    })

    secondTextButtonElement.addEventListener('click', () => {
        const originalText = secondTextBoxElement.value;
        secondTextBoxElement.value = '';
        secondTextBoxElement.value = shiftString(originalText, false);
    })

    function shiftString(str, up) {
        let shiftedString = '';
        for (let i = 0; i < str.length; i++) {
          const currentCharCode = str.charCodeAt(i);
          if (up) {
            const newCharCode = currentCharCode + 1;
            shiftedString += String.fromCharCode(newCharCode);
          } else {
            const newCharCode = currentCharCode - 1;
            shiftedString += String.fromCharCode(newCharCode);
          }
          
        }
        return shiftedString;
      }

}