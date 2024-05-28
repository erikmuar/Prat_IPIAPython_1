let edad = 19
// if
if(edad < 20 ){

    console.log("Eres menor de 20")
}
// if else
if(edad > 18){

    console.log("Eres mayor de edad")
}   else{
    console.log("Eres menor de edad")
    }
//if else if else
if(edad > 18){
    console.log("Eres mayor de edad")
} else if(edad == 18){
    console.log("Eres mayor de edad también")
} else{
    console.log("Eres menor de edad")
}

// varios else if 

let dia = prompt("Que dia de la semana es")
if(dia == "lunes"){
    console,log("Es lunes")
}else if(dia == "martes"){
    console.log("Es martes")
}else if(dia=="miercoles"){
    console.log("Es miercoles")
}else if(dia == "jueves"){
console.log("Es jueves")
}else if(dia == "viernes"){
    console.log("Es viernes")
}else{
    console.log(`${dia} es fin de semana`)
}
// switch 
// creas una variable y en switch escribes que pasaria en el caso de escribir cada variable diferente
let day = "lunes"
switch(day.toLowerCase()){

    case 1:
        console.log("It is monday");
        break;
    case 2: 
        console.log("It is tuesday");
        break;
    case 3: 
        console.log("It is wednesday");
        break;
    case 4: 
        console.log("It is thursday");
        break;
     case 5: 
        console.log("It is friday");
        break;
    case 6: 
        console.log("It is saturday");
        break;
    case 7: 
        console.log("It is sunday");
        break;
    default: 
        console.log(`${day} no es válido`)

}


// for y sus variantes

// for: Se usa para repetir acciones un número de veces, normalmente cuando el número de veces es desconocido 
// Bucle que se repite 10 veces.

for (let i = 0; i < 10; i++){
    console.log("Iteración",i)
}
// cuenta hasta 8 
for (let j = 0; j < 8; j++){
    console.log("iteración", j)
}
// cuenta atras 
for(let i = 10; i > 0; i--){
    console.log("iteración", i)
}
// Suma los primeros 100 números enteros 
suma = 0 
for(x = 0; x < 100; x++){
    suma+= x
console.log("Suma",suma)

}

suma = 0 
for(x = 0; x<100; x++){
    suma += x
console.log("Suma", suma)
}


suma = 0
for(x = 0; x<100; x++){
    suma = suma + x;
    console.log("Suma", suma)
}

// for in -> objetos

let coche = {

    "marca": "volvo",
    "modelo": "v80",
    "año": 2009,
}
coche."marca"