class Student extends Academician {
    String grade;
    String name;
    String age;

    Student(String name, String paramAge) {
        super(name);
        this.age = paramAge;
    }

    void studentSubject(String subject) {
        System.out.println("I am Student " + this.name);
    }
}