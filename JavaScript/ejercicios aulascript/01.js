

// Caso 1:
let precio = 100; // €
let iva = 21; // porcentaje
let impuesto = ( iva / 100 ) * precio; // 21 € 
let total = precio + impuesto;
console.log(precio, iva, "total:", total)

// Finalmente, escribimos el resultado en el id: ej-1-1
document.getElementById("ej-1-1").innerText = total;

// Caso 2:
precio = 200;
impuesto = ( iva / 100 ) * precio; // 42 €
total = precio + impuesto;
console.log(precio, iva, "total:", total)
// Finalmente, escribimos el resultado en el id: ej-1-2
document.getElementById("ej-1-2").innerText = total;
