function solve() {
  const textElement = document.getElementById('text');
  const namingConventionElement = document.getElementById('naming-convention');
  const resultElement = document.getElementById('result');

  const text = textElement.value;
  const namingConvention = namingConventionElement.value;

  const convertor = {
    'Pascal Case': (text) => text
      .toLowerCase()
      .split(' ')
      .map(word => word[0].toUpperCase() + word.slice(1))
      .join(''),
    'Camel Case': (text) => text
      .toLowerCase()
      .split(' ')
      .map((word, index) => index === 0 ? word : word[0].toUpperCase() + word.slice(1))
      .join('')
  };

  if (!convertor.hasOwnProperty(namingConvention)) {
    resultElement.textContent = 'Error!';
    return;
  }

  resultElement.textContent = convertor[namingConvention](text);
  
}