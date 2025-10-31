class SpaceAge:
    conversion={
        "Mercury":	0.2408467,
        "Venus":	0.61519726,
        "Earth":	1.0,
        "Mars":	1.8808158,
        "Jupiter":	11.862615,
        "Saturn":	29.447498,
        "Uranus":	84.016846,
        "Neptune":	164.79132
    }
    
    def __init__(self,seconds):
        self.earth_years=seconds/31557600
        
    def on_earth(self):
        return round(self.earth_years*self.conversion["Earth"],2)
        
    def on_mercury(self):
        return round(self.earth_years/self.conversion["Mercury"],2)
        
    def on_venus(self):
        return round(self.earth_years/self.conversion["Venus"],2)
        
    def on_mars(self):
        return round(self.earth_years/self.conversion["Mars"],2)
        
    def on_jupiter(self):
        return round(self.earth_years/self.conversion["Jupiter"],2)

    def on_saturn(self):
        return round(self.earth_years/self.conversion["Saturn"],2)

    def on_uranus(self):
        return round(self.earth_years/self.conversion["Uranus"],2)

    def on_neptune(self):
        return round(self.earth_years/self.conversion["Neptune"],2)