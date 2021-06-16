import 'package:flutter/cupertino.dart';
import 'package:remember_app/models/Tarefa.dart';

class TarefasProviders extends ChangeNotifier {

  //Lista de tarefas
 // ignore: deprecated_member_use
 List<Tarefas> _tarefas = new List<Tarefas>();

 List<Tarefas> get getTarefas{
   return _tarefas;
 }

// função para add tarefas na coleção
 void addTarefa(String titulo,String descricao)
 {
   Tarefas tarefa = new Tarefas(titulo, descricao);

   _tarefas.add(tarefa);

    notifyListeners();
 }

 // função para deletar tarefas pelo indice
 void removeTarefas(int index)
 {
   _tarefas.removeAt(index);
   notifyListeners();
 }


}