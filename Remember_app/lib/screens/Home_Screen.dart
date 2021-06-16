import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:remember_app/models/Tarefa.dart';
import 'package:provider/provider.dart';
import 'package:flutter_slidable/flutter_slidable.dart';
import 'package:remember_app/models/TarefasProvider.dart';

// ignore: camel_case_types
class Home_Screen extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.amber[100],
     appBar: AppBar(
       backgroundColor: Colors.deepPurple[600],
       toolbarHeight: 80,
       centerTitle: true,
       title: Text('Remember', style: TextStyle(fontSize: 20),)
     ),

      body: Padding(
        padding: const EdgeInsets.all(10.0),
        child: Consumer<TarefasProviders>(
          builder: (context,TarefasProviders data,child){
            return data.getTarefas.length !=0 ? ListView.builder(
              itemCount: data.getTarefas.length,
              itemBuilder: (context,index){
                return CardList(data.getTarefas[index],index);
              },
            ): GestureDetector(onTap: (){
              showAlertDialog(context);
            },child: Center(child: Text("ADICIONE SUAS TAREFAS",style: TextStyle(color: Colors.purple.shade900,),)));
          },
        ),
      ),

      floatingActionButton: FloatingActionButton(onPressed: () {
        showAlertDialog(context);
      },
          backgroundColor: Colors.deepPurple[600],
          child: Icon(Icons.add,color: Colors.white,),
      ),
    );

  }

}

// ignore: must_be_immutable
class CardList extends StatelessWidget {
  final Tarefas tarefas;
  int index;

  CardList(this.tarefas,this.index);

  @override
  Widget build(BuildContext context) {
    return Padding(
      padding: const EdgeInsets.all(2.0),
      child:Slidable(
        actionPane: SlidableDrawerActionPane(),
        actionExtentRatio: 0.25,
        child: Container(
          decoration: BoxDecoration(
            color: Colors.white,
            borderRadius: BorderRadius.only(
              bottomLeft: Radius.circular(15),
              topLeft: Radius.circular(15),

            )
          ),
          child: ListTile(
           leading: Icon(Icons.task_alt_outlined, color: Colors.green[400],),
              title: Text(tarefas.titulo, style: TextStyle(fontSize: 18),),
            subtitle: Text(tarefas.descricao, style: TextStyle(fontSize: 15),),
            trailing: Icon(Icons.arrow_forward_ios, color: Colors.red[300],),
          ),
        ),

        secondaryActions: <Widget>[
          IconSlideAction(
            caption: 'Delete',
            color: Colors.red,
            icon: Icons.delete,
            onTap: (){
              print("TAREFA EXCLUIDA");
              Provider.of<TarefasProviders>(context,listen: false).removeTarefas(index);
            }
          ),
        ],
      ),
    );
  }
}

showAlertDialog(BuildContext context) {

  // ignore: non_constant_identifier_names
  TextEditingController _Titulo = TextEditingController();
  // ignore: non_constant_identifier_names
  TextEditingController _Descricao = TextEditingController();
  // Criando Botão
  Widget okButton = MaterialButton(
    child: Text("CRIAR TAREFA"),
    onPressed: () {
      Provider.of<TarefasProviders>(context,listen: false).addTarefa(_Titulo.text, _Descricao.text);
      Navigator.of(context).pop();
    },
  );

  // Criando caixa de dialogo
  AlertDialog alert = AlertDialog(
    title: Text("NOVA TAREFA "),
    content: Column(
      mainAxisSize: MainAxisSize.min,
      children: [
        TextField(
          controller: _Titulo,
          decoration: InputDecoration(hintText: "Titulo"),
        ),
        TextField(
          controller: _Descricao,
          decoration: InputDecoration(hintText: "Descrição"),
        ),
      ],
    ),
    actions: [
      okButton,
    ],
  );

  // Mostrando caixa de dialogo
  showDialog(
    context: context,
    builder: (BuildContext context) {
      return alert;
    },
  );
}


