package enumeraciones;

public enum Continentes {
    
    AFRICA(54, "1.373.000.000"),
    EUROPA(44, "747,000,000"),
    ASIA(49, "4,678,000,000"),
    AMERICA(35,"1,010,000,000 "),
    OCEANIA(14,"43,800,000");
    
    private final int paises;
    private String habitantes;
    
    Continentes(int paises, String habitantes){
        this.paises = paises;
        this.habitantes = habitantes;
    }
    
    //Metodo Get
    public int getPaises(){
        return this.paises;
    }
    public String getHabitantes(){
        return this.habitantes;
    }
}
