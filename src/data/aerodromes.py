

class Aerodrome:
    
    def __init__(self, aerodrome):
        
        self.name = aerodrome
        self.altitude, self.herbe = self.get_altitude(aerodrome)
        
        
    def get_altitude(self, aerodrome):
        
        altitude = 0
        herbe = False
        match aerodrome:
            case 'Lasbordes':
                altitude = 460
            case 'Cahors':
                altitude = 912
            case 'Blagnac':
                altitude = 499
            case 'Graulhet':
                altitude = 518
            case 'Gaillac':
                altitude = 441
                herbe = True
            case 'Albi':
                altitude = 565
            case 'Pamiers':
                altitude = 1114
            case 'St. Girons':
                altitude = 1376
            case 'Auch':
                altitude = 411
            case 'Muret':
                altitude = 623
            case 'Castelnaudary':
                altitude = 553
            case 'Castelsarrasin':
                altitude = 243
            case 'Agen':
                altitude = 204
            case 'Custom':
                altitude = 0
                
        return altitude, herbe