class Academician {
    // field
    String name;
    String age;

    // // constructor
    Academician(String paramName, String paramAge) {
        this.name = paramName;
        this.age = paramAge;
    }

    // call other constructor
    Academician(String paramName) {
        this(paramName, null);
    }

    Academician() {
        this(null);
    }

    // method
    void studentSubject(String subject) {
        System.out.println(name + age + subject);
    }
}