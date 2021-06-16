import 'package:flutter/material.dart';
import 'package:remember_app/screens/Home_Screen.dart';
import 'package:remember_app/models/Tarefa.dart';
import 'package:remember_app/models/TarefasProvider.dart';
import 'package:provider/provider.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  
  @override
  Widget build(BuildContext context) {
    return ChangeNotifierProvider(
      create: (context)=>TarefasProviders(),
      child: MaterialApp(
        title: 'Remember ToDo',
        debugShowCheckedModeBanner: false,
        theme: ThemeData(
          primarySwatch: Colors.blue,
          visualDensity: VisualDensity.adaptivePlatformDensity,
        ),
        home: Home_Screen()
      ),
    );
  }
}

