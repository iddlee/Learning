function createObject(name,age){
	var obj=new Object();   // 通过Object实例化对象
	obj.name=name;
	obj.age=age;
	return obj;
}

function Person(name,age){
	this.name=name||"风清扬";
	this.age=age||20;
	this.setName=function(newName){
         this.name=newName;
	};
	this.getName=function(){
		return this.name;
	}
	return this;
}