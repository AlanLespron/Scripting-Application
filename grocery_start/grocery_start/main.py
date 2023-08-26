import csv


def write_list_of_dicts_to_csv(filename, data):
  with open(filename, 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=data[0].keys())
    writer.writeheader()
    writer.writerows(data)


def read_csv_to_dict(filename):
  with open(filename, 'r') as f:
    reader = csv.DictReader(f)
    return list(reader)


def main(sample_filename, batch_filename, output_filename):
  # Leer los datos del archivo sample_grocery.csv
  sample_data = read_csv_to_dict(sample_filename)
  sample_dict = {row['SKU']: row for row in sample_data}

  # Leer los datos del archivo grocery_batch_1.csv
  batch_data = read_csv_to_dict(batch_filename)

  # Comparar y actualizar los datos
  for row in batch_data:
    sku = row['SKU']
    cantidad = int(row['Quantity'])

    if sku in sample_dict:
      sample_dict[sku]['Quantity'] = str(
        int(sample_dict[sku]['Quantity']) + cantidad)
    else:
      sample_dict[sku] = row

  # Guardar los datos actualizados en el archivo grocery_db.csv
  write_list_of_dicts_to_csv(output_filename, list(sample_dict.values()))

  print("Proceso completado. Datos actualizados guardados en", output_filename)


if __name__ == '__main__':
  main('sample_grocery.csv', 'grocery_batch_1.csv', 'grocery_db.csv')
