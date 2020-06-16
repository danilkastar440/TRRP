<h1><b>Нормализация бд</b></h1><br>
Использованные СУБД: sqlite3 & MySQL <br>
Язык программирования: Python3 <br>
Как использовать: <br>
1. Для считывания и нормализации данных из sqlite3 в MySQL <br>
    python3 normalize.py --filename baza.db <br>
    
2. Для экспорта из MySQL в xlsx: <br> 
    python3 normalize.py --export <br>
  

  
Выполненные требования задания:
  1. Выбрана предметная область(машины) и спроектированы базы данных: <br>
    - Нормализованная в 5 таблицах 
      <table>
      <h2><b> Cars </b><h2>
      <tr>
        <th>model</th>
        <th>brand</th>
        <th>engine</th>
        <th>transmissins</th>
        <th>price</th>
        <th>wheel</th>
      </tr>
      <tr><td>2114</td><td>LADA</td><td>V123</td><td>M123</td><td>100000</td><td>Best kolesa</td></tr>
      <tr><td>2115</td><td>LADA</td><td>V124</td><td>M124</td><td>150000</td><td>Not best kolesa</td></tr>
      <tr><td>Rio</td><td>Kia</td><td>V14234</td><td>A1234</td><td>400000</td><td>Best kolesa</td></tr>
      <tr><td>Sportage</td><td>Kia</td><td>V12332</td><td>A123</td><td>500000</td><td>THE best kolesa</td></tr>
      <tr><td>911</td><td>Porsche</td><td>E2312</td><td>R123</td><td>3000000</td><td>THE Bbst kolesa</td></tr>
      </table>
      cars, brands, engines, transmissions, wheels
    - Ненормализованная в 1 таблице: car
    
    
