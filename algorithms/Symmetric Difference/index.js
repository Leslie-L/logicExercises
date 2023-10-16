function sym(...args) {
    console.log(args.length)
    let a = [...new Set(args[0])];
    let b;
    for (let i = 1; i < args.length; i++) {
         b = [...new Set(args[i])]
        const res = [...a.filter(item=>!b.includes(item)),...b.filter(item=>!a.includes(item))]
        a = [...res]

    }

    return a;
  }
  
  console.log(sym([1, 1, 2, 5], [2, 2, 3, 5], [3, 4, 5, 5]));
  //[1,4,5]