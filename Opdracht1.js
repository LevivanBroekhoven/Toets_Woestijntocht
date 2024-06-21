function kanBereikenTankstation(kilometersNaarTankstation, kilometersPerLiter, resterendeLiters) {
    kmgereden = resterendeLiters * kilometersPerLiter 
    if (kmgereden >= kilometersNaarTankstation)
    return true;

    else
    return false;
    
}

log1 = console.log(kanBereikenTankstation(80, 10, 8));
log2 = console.log(kanBereikenTankstation(90, 10, 8));
log3 = console.log(kanBereikenTankstation(80, 20, 4));
log4 = console.log(kanBereikenTankstation(150, 15, 10));
log5 = console.log(kanBereikenTankstation(40, 10, 5));
log6 = console.log(kanBereikenTankstation(100, 10, 9));