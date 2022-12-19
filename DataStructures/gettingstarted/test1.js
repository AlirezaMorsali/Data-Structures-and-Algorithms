// console.log('hello')
const somearray = ['nemo', 'bye']

function findnemo(array){
    for (let i=0; i<array.length; i++){
         if (array[i] == 'nemo'){
            console.log('found nemo')
        }
    }
}

findnemo(somearray)