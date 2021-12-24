.. tabs::

   .. tab:: MyST Markdown

      .. code-block:: markdown

         ```{admonition} What could be inside this warning?
         :class: warning, dropdown

         A whale of a joke!

         ![A whale of a joke](https://media.giphy.com/media/FaKV1cVKlVRxC/giphy.gif)

         (sorry)
         ```

   .. tab:: RestructuredText

      .. code-block:: rest

         .. admonition:: What could be inside this warning?
            :class: warning, dropdown

            A whale of a joke!

            .. image:: https://media.giphy.com/media/FaKV1cVKlVRxC/giphy.gif

            (sorry)

   .. tab:: 渲染结果

      .. admonition:: What could be inside this warning?
         :class: warning, dropdown

         A whale of a joke!

         .. image:: https://media.giphy.com/media/FaKV1cVKlVRxC/giphy.gif

         (sorry)
