
import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';

import 'package:remember_app/main.dart';

void main() {
  testWidgets('Conta incrementos', (WidgetTester tester) async {
    // Construção do app e add um quadro
    await tester.pumpWidget(MyApp());

    // Verifica se o contador estar em 0.
    expect(find.text('0'), findsOneWidget);
    expect(find.text('1'), findsNothing);

    // Toque no '+' para adicionar uma tarefa
    await tester.tap(find.byIcon(Icons.add));
    await tester.pump();

    // verifica se o contador aumentou
    expect(find.text('0'), findsNothing);
    expect(find.text('1'), findsOneWidget);
  });
}
