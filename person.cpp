
#include <cstdlib>
// Person class 

class Person{
	public:
		Person(int);
		int get();
		void set(int);
		int fib(); //fib_py
	private:
		int private_fib(int);
		int age;
	};	
 
Person::Person(int n){
	age = n;
	}
 
int Person::get(){
	return age;
	}
 
void Person::set(int n){
	age = n;
	}
int Person::fib(){
	return private_fib(age);
	}
int Person::private_fib(int n){
	if (n <= 1)
	{
		return n;
	}
	else
	{
		return private_fib(n-1) + private_fib(n-2);
	}

}

extern "C"{
	Person* Person_new(int n) {return new Person(n);}
	int Person_get(Person* person) {return person->get();}
	void Person_set(Person* person, int n) {person->set(n);}
	int Person_fib(Person * person) {return person->fib();}
	void Person_delete(Person* person){
		if (person){
			delete person;
			person = nullptr;
			}
		}
	}
