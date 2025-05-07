
    let bodyParts=["face","eyebrows","hips","legs","nose","ears","mouth"];
    bodyParts=bodyParts[Math.floor(Math.random()*bodyParts.length)]
    let negativeAdj=["dirty","smelly","thin","fat","dumb","useless","idiot"];
    negativeAdj=negativeAdj[Math.floor(Math.random()*negativeAdj.length)]
    let lookALike=["vulture","pig","sloth","hyena","rat","monkey","rakoon"];
    lookALike=lookALike[Math.floor(Math.random()*lookALike.length)]

    console.log(`Your ${bodyParts} is like a ${negativeAdj} ${lookALike}!!!`)
