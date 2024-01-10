function loopOverObject(object){
    for (item in object){
        console.log(`Key: ${item}; Value: ${object[item]}`)
    }

}

loopOverObject({ 'foo': 'bar', 'ding': 'dong' });
