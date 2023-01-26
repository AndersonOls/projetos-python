sql = """UPDATE alunos
              SET matricula =""" + up_matricula + """, nome=""" + "\"" + up_nome + "\"" \
      + """, curso = """ + "\"" + up_curso + "\"" + """, turma= """ + "\"" + up_turma + \
      "\"" + """ WHERE idAluno= """ + up_id