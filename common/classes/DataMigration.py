from setup.models import Dataset


class DataMigration:

    def saveRecord(self, key, app_name, model_name, Modelpass, Record):

        dataset = Dataset.objects.filter(key=key, app_name=app_name, model_name=model_name).first()
        
        Record.is_dataMigration = True

        if dataset:
            Record.id = dataset.record_id

            datarecord = Modelpass.objects.filter(id=dataset.record_id).first()

            if datarecord:
                if not datarecord.is_modified:
                    Record.created_at = datarecord.created_at
                    Record.created_by = datarecord.created_by
                    Record.is_modified = False
                    Record.save()
            
        else:
            Record.is_modified = False
            Record.save()
        
        if dataset is None:
            Dataset(key=key, app_name=app_name, model_name=model_name, record_id=Record.id).save()
        
